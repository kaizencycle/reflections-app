// app/page.tsx (example)
import Layout from "@/components/Layout";
import Companions from "@/components/Companions";
import Chat from "@/components/Chat";

export default function Page() {
  return <Layout sidebar={<Companions />}><Chat/></Layout>;
}
