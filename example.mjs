import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5-nano",
    input: "Write a one-sentence bedtime story about a goblin king."
});

console.log(response.output_text);