'use client'

<<<<<<< HEAD
type SummaryResponse = {
  city: string
  top_issue: string
  average_sentiment: number
  mismatch_hotspots: number
}

export default function SummaryCards({ data }: { data: SummaryResponse | null }) {
=======
interface SummaryCardsProps {
  data: {
    total_data_points?: number;
    mismatch_hotspots: number;
    average_sentiment: number;
    top_issue: string;
    city: string;
  } | null;
  insightsCount: number;
}

export default function SummaryCards({ data, insightsCount }: SummaryCardsProps) {
>>>>>>> a7dd7179371cf60abafa5351a198e4f19a3b22ff
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">City</h3>
        <p className="text-2xl">{data?.city ?? '—'}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
<<<<<<< HEAD
        <h3 className="text-lg font-semibold">Top Issue</h3>
        <p className="text-2xl">{data?.top_issue ?? '—'}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Avg. Sentiment</h3>
        <p className="text-2xl">{data ? data.average_sentiment.toFixed(2) : '—'}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Mismatch Hotspots</h3>
        <p className="text-2xl">{data?.mismatch_hotspots ?? '—'}</p>
=======
        <h3 className="text-lg font-semibold">Mismatches</h3>
        <p className="text-2xl">{data?.mismatch_hotspots || 0}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Insights</h3>
        <p className="text-2xl">{data?.average_sentiment || 0}</p>
>>>>>>> a7dd7179371cf60abafa5351a198e4f19a3b22ff
      </div>
    </div>
  )
}
