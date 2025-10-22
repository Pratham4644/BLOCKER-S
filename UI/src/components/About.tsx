import { Code2, Link2, Zap, Mic2, Box } from "lucide-react";

const About = () => {
  const techStack = [
    { name: "Python", icon: "🐍", color: "from-blue-500 to-yellow-500" },
    { name: "Composio", icon: "🔗", color: "from-purple-500 to-pink-500" },
    { name: "OpenAI", icon: "⚡", color: "from-green-400 to-cyan-400" },
    { name: "ElevenLabs", icon: "🎙️", color: "from-orange-500 to-red-500" },
    { name: "LangChain", icon: "🧩", color: "from-indigo-500 to-purple-500" },
  ];

  return (
    <section id="about" className="py-20 px-4 bg-gradient-hero">
      <div className="container mx-auto max-w-5xl">
        <div className="text-center mb-16 space-y-4">
          <div className="inline-block px-4 py-2 bg-accent/10 rounded-full border border-accent/20 text-accent text-sm mb-4">
            🏆 Built for Hackathon Excellence
          </div>
          <h2 className="text-4xl md:text-5xl font-bold">
            Empowering{" "}
            <span className="bg-gradient-accent bg-clip-text text-transparent">
              Indian Students
            </span>
          </h2>
        </div>

        <div className="bg-card/50 backdrop-blur-sm border border-border rounded-2xl p-8 md:p-12 shadow-card mb-12">
          <p className="text-lg md:text-xl text-center text-foreground/90 leading-relaxed mb-8">
            CodeSahayak was built in <span className="text-accent font-semibold">3 days</span> by{" "}
            <span className="text-primary font-semibold">Prathamesh Shinde</span> to revolutionize 
            how Indian students learn Data Structures and Algorithms. Using cutting-edge AI and 
            workflow automation, it provides <span className="text-accent-glow font-semibold">
            bilingual mentorship</span> that understands both code and context.
          </p>

          <div className="grid md:grid-cols-3 gap-8 text-center">
            <div className="space-y-2">
              <div className="text-4xl font-bold text-primary">6+</div>
              <div className="text-muted-foreground">Tool Integrations</div>
            </div>
            <div className="space-y-2">
              <div className="text-4xl font-bold text-accent">2</div>
              <div className="text-muted-foreground">Languages Supported</div>
            </div>
            <div className="space-y-2">
              <div className="text-4xl font-bold text-primary-glow">24/7</div>
              <div className="text-muted-foreground">AI Availability</div>
            </div>
          </div>
        </div>

        {/* Tech Stack */}
        <div>
          <h3 className="text-2xl font-bold text-center mb-8">Powered By</h3>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-6">
            {techStack.map((tech, index) => (
              <div
                key={tech.name}
                className={`group bg-gradient-to-br ${tech.color} rounded-2xl p-6 flex flex-col items-center gap-3 shadow-card hover:shadow-glow transition-all duration-300 hover:scale-110 cursor-pointer animate-fade-in`}
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="text-4xl group-hover:animate-float">{tech.icon}</div>
                <span className="text-white font-semibold text-sm text-center">{tech.name}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Mission Statement */}
        <div className="mt-16 text-center max-w-3xl mx-auto">
          <blockquote className="text-xl italic text-muted-foreground">
            "Breaking language barriers in tech education, one line of code at a time."
          </blockquote>
        </div>
      </div>
    </section>
  );
};

export default About;
