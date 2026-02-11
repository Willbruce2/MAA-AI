import { useState } from 'react';

export default function App() {
  const [task, setTask] = useState('ncoer');
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  const send = async () => {
    const res = await fetch('/chat', {
      method:'POST',
      headers: { 'Content-Type':'application/json' },
      body: JSON.stringify({task, prompt:input})
    });
    const data = await res.json();
    setOutput(data.response);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">MAA-AI Dashboard</h1>
      <select value={task} onChange={e=>setTask(e.target.value)}>
        <option value="ncoer">NCOER</option>
        <option value="award">Award</option>
        <option value="mfr">MFR</option>
        <option value="counseling">Counseling</option>
      </select>
      <textarea value={input} onChange={e=>setInput(e.target.value)} />
      <button onClick={send}>Generate</button>
      <pre>{output}</pre>
    </div>
  );
}
