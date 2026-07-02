export type Conversion="phiToInt"|"IntToPhi"
export type Operator = "+" | "-" | "*";

interface PyodideInterface{
    runPythonAsync:(code:string)=>Promise<unknown>
    globals:{
        set:(name:string,value:unknown)=>void;
    };
}

declare global{//сообщение о глобальном объекте
    interface Window{
        loadPyodide:(config?:{indexURL?:string})=>Promise<PyodideInterface>
    }
}

let pyodidePromise:Promise<PyodideInterface>|null=null; //переменная для хранения процесса загрузки

function getPyodide(): Promise<PyodideInterface> {
  if (!pyodidePromise) {
    pyodidePromise = window
      .loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/" })
      .then(async (pyodide) => {
        await pyodide.runPythonAsync(`
          import micropip
          await micropip.install("phi-numeral-system") 
        `);
        return pyodide;
      });
  }
  return pyodidePromise;
}

export async function convertNumber(value:string,station:Conversion):Promise<string>{
    const pyodide=await getPyodide();
    pyodide.globals.set("input_value", value);
    pyodide.globals.set("station", station);
    const result = await pyodide.runPythonAsync(`
        from phi_numeral_system import phi_to_int, int_to_phi
        (phi_to_int(input_value) if station == "phiToInt" else int_to_phi(input_value))
`);
    return String(result);
}

export async function calculate(left: string,operator: Operator,right: string): Promise<{ phi: string; decimal: string }> {
    const pyodide = await getPyodide();
    pyodide.globals.set("left_value", left);
    pyodide.globals.set("right_value", right);
     pyodide.globals.set("op", operator);
 
    const result = await pyodide.runPythonAsync(`
        from phi_numeral_system import phi_calculate
        phi_calculate(left_value, right_value, op)
  `);
    const asObject = (result as any).toJs
        ? Object.fromEntries((result as any).toJs())
        : (result as { phi: string; decimal: string });
 
     return { phi: String(asObject.phi), decimal: String(asObject.decimal) };
}