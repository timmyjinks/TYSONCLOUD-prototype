export const load = async () => {
  const response = await fetch("http://localhost:8000/container_info")
  const data = await response.json()
  return {container_info: data}
}
