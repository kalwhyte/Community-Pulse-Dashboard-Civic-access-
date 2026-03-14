'use client'

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
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Total Data Points</h3>
        <p className="text-2xl">{data?.total_data_points || 0}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Mismatches</h3>
        <p className="text-2xl">{data?.mismatch_hotspots || 0}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold">Insights</h3>
        <p className="text-2xl">{data?.average_sentiment || 0}</p>
      </div>
    </div>
  )
}
