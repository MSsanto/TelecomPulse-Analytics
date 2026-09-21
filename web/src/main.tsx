import React from 'react'
import ReactDOM from 'react-dom/client'
import './styles.css'

function App() {
  return (
    <main className="shell">
      <p className="eyebrow">SPRINT 0 FOUNDATION</p>
      <h1>TelecomPulse Analytics</h1>
      <p>
        Governed analytics foundation for telecom and NOC data. Functional dashboard features
        begin only after Sprint 0 human homologation.
      </p>
      <section aria-label="Foundation status">
        <h2>Foundation status</h2>
        <ul>
          <li>Python pipeline scaffolded</li>
          <li>Synthetic reference dataset</li>
          <li>Automated tests and lint</li>
          <li>React/TypeScript/Vite build baseline</li>
          <li>CI gate ready</li>
        </ul>
      </section>
    </main>
  )
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
