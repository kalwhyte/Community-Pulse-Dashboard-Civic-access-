'use client'

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

export default function InsightPanel({ insight }: Props) {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">AI Insights</h3>
      <p>Insights from Gemini API will appear here.</p>
    </div>
  )
}
