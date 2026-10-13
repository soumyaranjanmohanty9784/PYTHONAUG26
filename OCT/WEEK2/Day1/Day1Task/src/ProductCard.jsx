
function ProductCard({ product }) {
  return (
    <div className="w-72 overflow-hidden rounded-xl bg-white shadow-lg transition hover:-translate-y-1 hover:shadow-xl">
      <img
        src={product.image}
        alt={product.name}
        className="h-48 w-full object-cover"
      />

      <div className="p-5">
        <h2 className="mb-2 text-xl font-bold text-gray-800">
          {product.name}
        </h2>

        <p className="mb-4 text-sm text-gray-600">
          {product.description}
        </p>

        <div className="flex items-center justify-between">
          <span className="text-lg font-bold text-green-600">
            ₹{product.price}
          </span>

          <button className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}

export default ProductCard;
