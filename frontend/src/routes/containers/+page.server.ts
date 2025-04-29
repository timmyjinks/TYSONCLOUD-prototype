export const load = async () => {
  const response = await fetch("http://backend:8000/containers")
  const data = await response.json()
  return {containers: data}
}

