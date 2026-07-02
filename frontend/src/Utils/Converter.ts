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
await micropip.install("golden-ration-ns")
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
import goldenratio as gr
from goldenratio.Logos import GoldenNumber

if station == "IntToPhi":
    n = int(input_value)
    gn = GoldenNumber(n, 0)
    phi = gr.translate_to_fi(gn)
    output = str(phi)
else:
    digits = {}
    int_part, _, frac_part = input_value.partition(".")
    n = len(int_part)
    for i, ch in enumerate(int_part):
        power = n - 1 - i
        if ch != "0":
            digits[power] = int(ch)
    for i, ch in enumerate(frac_part):
        power = -(i + 1)
        if ch != "0":
            digits[power] = int(ch)

    result = GoldenNumber(0, 0)
    for k, d in digits.items():
        deg = gr.fi_degree(k)
        result = result + GoldenNumber(deg.a * d, deg.b * d)
    output = str(int(result))

output
`);
    return String(result);
}

export async function calculate(left: string,operator: Operator,right: string): Promise<{ phi: string; decimal: string }> {
    const pyodide = await getPyodide();
    pyodide.globals.set("left_value", left);
    pyodide.globals.set("right_value", right);
     pyodide.globals.set("op", operator);
 
    const result = await pyodide.runPythonAsync(`
import goldenratio as gr
from goldenratio.Logos import GoldenNumber

a = GoldenNumber(int(left_value), 0)
b = GoldenNumber(int(right_value), 0)

phi_a = gr.translate_to_fi(a)
phi_b = gr.translate_to_fi(b)

if op == "+":
    result = phi_a + phi_b
elif op == "-":
    result = phi_a - phi_b
elif op == "*":
    result = phi_a * phi_b
else:
    raise ValueError("Unknown operator: " + op)

{"phi": str(result), "decimal": str(int(result))}
`);
    const asObject = (result as any).toJs
        ? Object.fromEntries((result as any).toJs())
        : (result as { phi: string; decimal: string });
 
     return { phi: String(asObject.phi), decimal: String(asObject.decimal) };
}