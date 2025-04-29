import type { RequestHandler} from "@sveltejs/kit"

export const PUT: RequestHandler = async({request}) => {
  const form = await request.json()

  const response = await fetch("http://backend:8000/container", 
    {
      method: "PUT",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(form)
    }  
  )
  const data = await response.json()

  return new Response(JSON.stringify(data), {status: 201})
}

export const DELETE: RequestHandler = async({request}) => {
  const form = await request.json()

  const response = await fetch("http://backend:8000/container", 
    {
      method: "DELETE",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(form)
    }  
  )
  const data = await response.json()

  return new Response(JSON.stringify(data), {status: 201})
}
