import type { RequestHandler} from "@sveltejs/kit"

export const POST: RequestHandler = async({request}) => {
  const form = await request.json()

  const response = await fetch("http://backend:8000/containers", 
    {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(form)
    }  
  )
  const data = await response.json()

  return new Response(JSON.stringify(data), {status: 201})
}

