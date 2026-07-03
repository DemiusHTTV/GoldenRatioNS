import { useState } from 'react'
import PurpleBlock from './Components/purpleBlock'
import { convertNumber, calculate, type Operator } from './Utils/Converter'

function SwapButton({ onClick }: { onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} className="swap-btn">
      Поменять
    </button>
  )
}

function getFriendlyError(err: unknown): string {
  const message = err instanceof Error ? err.message : String(err)
  if (message.includes('Cannot convert to int')) {
    return 'Эта запись не сворачивается в целое число — проверьте разряды.'
  }
  if (message.includes('invalid literal for int')) {
    return 'Введите корректное число.'
  }
  return 'Не удалось выполнить вычисление. Проверьте введённые данные.'
}

function App() {
  // направление перевода
  const [toPhi, setToPhi] = useState(true)
  const [translateInput, setTranslateInput] = useState('')
  const [translateResult, setTranslateResult] = useState('')
  const [translateError, setTranslateError] = useState('')
  const [translateLoading, setTranslateLoading] = useState(false)

  // порядок арифметики
  const [phiFirst, setPhiFirst] = useState(true)
  const [numA, setNumA] = useState('')
  const [operator, setOperator] = useState<Operator>('+')
  const [numB, setNumB] = useState('')
  const [resultPhi, setResultPhi] = useState('')
  const [resultDecimal, setResultDecimal] = useState('')
  const [calcError, setCalcError] = useState('')
  const [calcLoading, setCalcLoading] = useState(false)

  const handleTranslate = async () => {
    setTranslateLoading(true)
    setTranslateError('')
    try {
      const station = toPhi ? 'IntToPhi' : 'phiToInt'
      const result = await convertNumber(translateInput, station)
      setTranslateResult(result)
    } catch (err) {
      setTranslateResult('')
      setTranslateError(getFriendlyError(err))
    } finally {
      setTranslateLoading(false)
    }
  }

  const handleCalculate = async () => {
    setCalcLoading(true)
    setCalcError('')
    try {
      const { phi, decimal } = await calculate(numA, operator, numB)
      setResultPhi(phi)
      setResultDecimal(decimal)
    } catch (err) {
      setResultPhi('')
      setResultDecimal('')
      setCalcError(getFriendlyError(err))
    } finally {
      setCalcLoading(false)
    }
  }

  return (
    <div className="page">
      <div className="page-header">
        <h1>Фи-еричная система счисления</h1>
        <p>Система с основанием φ=(1+√5)/2</p>
      </div>

      <PurpleBlock
        title="Перевод числа"
        subtitle="Переведите число между десятичной и фи-еричной записью"
        action={<SwapButton onClick={() => setToPhi((prev) => !prev)} />}
        content={
          <div className="field-group">
            <div className="form-row">
              <input
                type="text"
                className="text-input"
                placeholder={
                  toPhi
                    ? 'Введите число в десятичной записи...'
                    : 'Введите число в фи-еричной записи...'
                }
                value={translateInput}
                onChange={(e) => setTranslateInput(e.target.value)}
              />
              <button
                type="button"
                onClick={handleTranslate}
                disabled={translateLoading}
                className="primary-btn"
              >
                {translateLoading ? 'Считаю...' : 'Перевести'}
              </button>
            </div>

            <div className="result-box">
              <span
                className="result-label"
                onClick={() => setToPhi((prev) => !prev)}
                title="Поменять направление перевода"
              >
                {toPhi ? 'Фи-еричная запись' : 'Десятичная запись'}
              </span>
              <div className="result-value">{translateResult}</div>
            </div>
            {translateError && <p className="error-text">{translateError}</p>}
          </div>
        }
      />

      <PurpleBlock
        title="Арифметика"
        subtitle="Сложение, вычитание и умножение чисел в фи-еричной системе"
        content={
          <div className="field-group">
            <div className="form-row">
              <input
                type="text"
                className="number-input"
                value={numA}
                onChange={(e) => setNumA(e.target.value)}
              />
              <select
                className="select-input"
                value={operator}
                onChange={(e) => setOperator(e.target.value as Operator)}
              >
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">×</option>
              </select>
              <input
                type="text"
                className="number-input"
                value={numB}
                onChange={(e) => setNumB(e.target.value)}
              />
              <button
                type="button"
                onClick={handleCalculate}
                disabled={calcLoading}
                className="primary-btn"
              >
                {calcLoading ? 'Считаю...' : 'Посчитать'}
              </button>
            </div>

            <div className="results-row">
              {phiFirst ? (
                <>
                  <div className="result-box">
                    <span
                      className="result-label"
                      onClick={() => setPhiFirst((prev) => !prev)}
                      title="Поменять порядок"
                    >
                      Фи-еричная запись
                    </span>
                    <div className="result-value">{resultPhi}</div>
                  </div>
                  <div className="result-box">
                    <span
                      className="result-label"
                      onClick={() => setPhiFirst((prev) => !prev)}
                      title="Поменять порядок"
                    >
                      Десятичная запись
                    </span>
                    <div className="result-value">{resultDecimal}</div>
                  </div>
                </>
              ) : (
                <>
                  <div className="result-box">
                    <span
                      className="result-label"
                      onClick={() => setPhiFirst((prev) => !prev)}
                      title="Поменять порядок"
                    >
                      Десятичная запись
                    </span>
                    <div className="result-value">{resultDecimal}</div>
                  </div>
                  <div className="result-box">
                    <span
                      className="result-label"
                      onClick={() => setPhiFirst((prev) => !prev)}
                      title="Поменять порядок"
                    >
                      Фи-еричная запись
                    </span>
                    <div className="result-value">{resultPhi}</div>
                  </div>
                </>
              )}
            </div>
            {calcError && <p className="error-text">{calcError}</p>}
          </div>
        }
      />
    </div>
  )
}

export default App