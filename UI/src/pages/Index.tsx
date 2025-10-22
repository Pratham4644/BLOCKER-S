import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Features from "@/components/Features";
import Demo from "@/components/Demo";
import Workflow from "@/components/Workflow";
import About from "@/components/About";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />
      <Hero />
      <Features />
      <Demo />
      <Workflow />
      <About />
      <Footer />
    </div>
  );
};

export default Index;
