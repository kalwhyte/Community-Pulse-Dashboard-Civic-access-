'use client'

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

type Insight = {
  location: string
  mismatch_score: number
}

type ChartPoint = {
  name: string
  mismatches: number
}

const fallbackData: ChartPoint[] = [
  { name: 'Jan', mismatches: 4 },
  { name: 'Feb', mismatches: 3 },
  { name: 'Mar', mismatches: 2 },
  { name: 'Apr', mismatches: 5 },
]

<<<<<<< HEAD
<<<<<<< HEAD
export default function MismatchChart({ insights }: { insights: Insight[] }) {
  const chartData: ChartPoint[] = insights.length
    ? insights.map((item) => ({
        name: item.location,
        mismatches: Number(item.mismatch_score.toFixed(2)),
      }))
    : fallbackData

=======
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
type Insight = {
  location: string;
  category: string;
  social_score: number;
  official_score: number;
  mismatch_score: number;
  explanation: string;
};

type Props = {
  insight: Insight[];
};

export default function MismatchChart({ insight }: Props) {
<<<<<<< HEAD
>>>>>>> a7dd7179371cf60abafa5351a198e4f19a3b22ff
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
  return (
    <div className="bg-white p-4 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">Mismatch Snapshot</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
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
