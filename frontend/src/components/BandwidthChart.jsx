import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

function BandwidthChart({ data }) {
  const formatted = data.map(([timestamp, size]) => ({
    time: new Date(timestamp * 1000).toLocaleTimeString(),
    bytes: size,
  }));

  return (
    <div>
      <h2>Bandwidth Usage</h2>
      <LineChart width={600} height={300} data={formatted}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="bytes" />
      </LineChart>
    </div>
  );
}

export default BandwidthChart;
