'use client'

type Insight = {
<<<<<<< HEAD
<<<<<<< HEAD
  location: string
  category: string
  mismatch_score: number
  explanation: string
}

export default function InsightPanel({ insights }: { insights: Insight[] }) {
=======
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
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

export default function InsightPanel({ insight }: Props) {
<<<<<<< HEAD
>>>>>>> a7dd7179371cf60abafa5351a198e4f19a3b22ff
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
  return (
    <div className="bg-white p-4 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">AI Insights</h3>
      {insights.length === 0 ? (
        <p>No insights yet. Run a crawl to generate data.</p>
      ) : (
        <ul className="space-y-4">
          {insights.map((insight, index) => (
            <li key={`${insight.location}-${index}`} className="border-b pb-3 last:border-b-0">
              <div className="flex items-center justify-between">
                <span className="font-semibold">{insight.location}</span>
                <span className="text-sm text-slate-600">Mismatch: {insight.mismatch_score.toFixed(2)}</span>
              </div>
              <div className="text-sm text-slate-600">{insight.category}</div>
              <p className="text-sm mt-2">{insight.explanation}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
