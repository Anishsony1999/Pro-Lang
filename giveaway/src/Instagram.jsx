'use client';

import React, { useState, useEffect } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs";
import { Button } from "./components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "./components/ui/card";
import { ScrollArea } from "./components/ui/scroll-area";
import { Avatar, AvatarFallback, AvatarImage } from "./components/ui/avatar";


// Mock list of usernames
const mockUsernames = [
  "user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10",
  "user11", "user12", "user13", "user14", "user15", "user16", "user17", "user18", "user19", "user20"
];

export default function Instagram() {
  const [selectedUsers, setSelectedUsers] = useState([]);
  const [isActive, setIsActive] = useState(false);
  const [time, setTime] = useState(10);
  const [rotation, setRotation] = useState(0);
  const [activeTab, setActiveTab] = useState("picker");

  useEffect(() => {
    let interval;

    if (isActive && time > 0) {
      interval = setInterval(() => {
        setTime((prevTime) => {
          const newTime = prevTime - 1;
          setRotation(360 - (newTime / 10) * 360);
          return newTime > 0 ? newTime : 0;
        });
      }, 1000);
    } else if (time === 0) {
      setIsActive(false);
      pickRandomUsers();
      setActiveTab("winners");
    }

    return () => clearInterval(interval);
  }, [isActive, time]);

  const toggleTimer = () => {
    if (time === 0) {
      setTime(10);
      setRotation(0);
      setSelectedUsers([]);
    }
    setIsActive(!isActive);
  };

  const pickRandomUsers = () => {
    const shuffled = [...mockUsernames].sort(() => 0.5 - Math.random());
    setSelectedUsers(shuffled.slice(0, 3));
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-100 flex items-center justify-center p-4">
      <Card className="w-full max-w-3xl shadow-xl">
        <CardHeader className="bg-gradient-to-r from-pink-500 to-purple-600 text-white">
          <CardTitle className="text-2xl font-bold">Instagram Comment Picker</CardTitle>
          <CardDescription className="text-pink-100">Pick random usernames from comments</CardDescription>
        </CardHeader>
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="picker">Comment Picker</TabsTrigger>
            <TabsTrigger value="winners">Winners</TabsTrigger>
          </TabsList>
          <TabsContent value="picker">
            <CardContent className="p-6">
              <div className="flex flex-col items-center">
                <div className="relative w-48 h-48 mb-4">
                  <svg className="w-full h-full" viewBox="0 0 100 100">
                    <circle
                      cx="50"
                      cy="50"
                      r="45"
                      fill="none"
                      stroke="#e0e0e0"
                      strokeWidth="10"
                    />
                    <circle
                      cx="50"
                      cy="50"
                      r="45"
                      fill="none"
                      stroke="#f472b6"
                      strokeWidth="10"
                      strokeDasharray="282.7"
                      strokeDashoffset={282.7 - (rotation / 360) * 282.7}
                      transform="rotate(-90 50 50)"
                    />
                  </svg>
                  <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-4xl font-bold text-gray-800">
                    {time}
                  </div>
                </div>
                <Button 
                  onClick={toggleTimer} 
                  className="w-full bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-600 hover:to-purple-700 text-white"
                >
                  {isActive ? 'Pause' : time === 0 ? 'Restart' : 'Start Countdown'}
                </Button>
              </div>
            </CardContent>
          </TabsContent>
          <TabsContent value="winners">
            <CardContent className="p-6">
              <h3 className="text-lg font-semibold mb-4">Selected Winners:</h3>
              <ScrollArea className="h-[200px] w-full rounded-md border p-4">
                {selectedUsers.length > 0 ? (
                  selectedUsers.map((user, index) => (
                    <div key={index} className="flex items-center space-x-4 mb-4">
                      <Avatar>
                        <AvatarImage src={`https://api.dicebear.com/6.x/avataaars/svg?seed=${user}`} alt={`${user}'s avatar`} />
                        <AvatarFallback>{user.slice(0, 2).toUpperCase()}</AvatarFallback>
                      </Avatar>
                      <div>
                        <p className="text-sm font-medium leading-none">{user}</p>
                        <p className="text-sm text-muted-foreground">Winner #{index + 1}</p>
                      </div>
                    </div>
                  ))
                ) : (
                  <p className="text-gray-500">No winners selected yet. Start the countdown to select winners.</p>
                )}
              </ScrollArea>
            </CardContent>
          </TabsContent>
        </Tabs>
        <CardFooter className="bg-gray-50 text-gray-600 text-sm">
          Disclaimer: This is a demo app and does not connect to real Instagram data.
        </CardFooter>
      </Card>
    </div>
  );
}
