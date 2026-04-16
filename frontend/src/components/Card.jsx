function Card({ title, value, unit }) {
  return (
    <div style={styles.card}>
      <h4>{title}</h4>
      <h2>
        {value} <span style={styles.unit}>{unit}</span>
      </h2>
    </div>
  );
}

const styles = {
  card: {
    backgroundColor: "#111827",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "10px",
    border: "1px solid #1f2937",
  },
  unit: {
    fontSize: "14px",
    opacity: 0.7,
  },
};

export default Card;
