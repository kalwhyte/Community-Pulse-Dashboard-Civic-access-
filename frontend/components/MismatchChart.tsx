'use client'

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const data = [
  { name: 'Jan', mismatches: 4 },
  { name: 'Feb', mismatches: 3 },
  { name: 'Mar', mismatches: 2 },
  { name: 'Apr', mismatches: 5 },
]

export default function MismatchChart() {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">Mismatch Trends</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="mismatches" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
