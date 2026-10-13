
import ProductCard from "./productCard";

const products = [
  {
    id: 1,
    name: "Laptop",
    price: 55000,
    image:
      "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400",
    description: "Powerful laptop for work and study",
  },
  {
    id: 2,
    name: "Headphones",
    price: 2500,
    image:
      "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
    description: "High-quality wireless headphones",
  },
  {
    id: 3,
    name: "Smart Watch",
    price: 4000,
    image:
      "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
    description: "Smart watch for everyday use",
  },
];

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="mb-8 text-center text-3xl font-bold">
        Our Products
      </h1>

      <div className="flex flex-wrap justify-center gap-6">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default App;
