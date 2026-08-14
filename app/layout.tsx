import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Internal Question Revision",
  description: "Study and test platform for internal question banks"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
