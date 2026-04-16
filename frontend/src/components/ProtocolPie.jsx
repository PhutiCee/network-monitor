import { PieChart, Pie, Cell, Tooltip } from "recharts";

function ProtocolPie({ data }) {
  const formatted = Object.entries(data).map(([key, value]) => ({
    name: key,
    value,
  }));

  return (
    <div>
      <h2>Protocol Distribution</h2>
      <PieChart width={400} height={300}>
        <Pie data={formatted} dataKey="value" nameKey="name" outerRadius={100}>
          {formatted.map((entry, index) => (
            <Cell key={index} />
          ))}
        </Pie>
        <Tooltip />
      </PieChart>
    </div>
  );
}

export default ProtocolPie;
