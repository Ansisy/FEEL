from zhipuai import ZhipuAI
client = ZhipuAI(api_key="your_api_key")

response = client.chat.completions.create(
        model="glm-4", 
        messages=[
            {
"role": "user",
"content":
"""You will play the role of a psychologist who is well versed in emotional support. There will be a dialog between the help seeker (i.e., the person seeking support) and the supporter (i.e., the person providing support). The dialog will consist of the help-seeker asking the supporter for help with some emotional problem, and the supporter will give the appropriate emotional support and advice.
Your task is to act as an impartial scoring judge and rate each round of the dialog in terms of the following aspects in order to evaluate the quality of the dialog between the two parties. Please read and fully understand the following scoring criteria.

### Evaluation Criteria:
(1) Informativeness: the degree of detail in which the client describes his/her emotional problems.

### Options:

3 points: detailed description
2 points: general description
1 point: brief description
0: No description at all

### Give an example:

When a helper seeks emotional support from a supporter:

Describe in detail (3 points): "Since I lost my job, I have been feeling very anxious and depressed. I worry about my future and my finances, and it keeps me up at night." (The client provides detailed information about his/her emotional problems, including the causes and specific effects of the feelings)
General description (2 points), "I have been feeling a little down lately because I can't find a job." (The helper only describes the emotional problem or his/her own feelings, or provides relatively little information and may be missing some key details)
Brief description (1 point), "I've been a little upset lately." (The helper provides a very brief description of the emotional problem and feelings)
Basically no description (0 points): "I have some problems." (The helper does not provide any specific information about the emotional state)

(2) Comprehensibility: how well the supporter understands the help-seeker's experiences and feelings.

### Options:

3 points: complete understanding
2 points: Moderate understanding
1 point: Not very understanding
0: No understanding at all

### Give an example:

When the helper mentions, "I felt so alone after my dog died, he was my best friend." The helper responds:

Completely understood (3 points): "That must have been hard. It's always hard to lose a pet, especially when they were your best friend. Would you like to talk about it? It sounds like a very special companion." (The supporter is able to reach a state of full empathy with the helper and deeply explore the reasons for the helper's emotional problems)
Moderate Understanding (2 points): "I'm sorry to hear that. The death of a pet is always a sad event." (The supporter demonstrates basic empathy and understanding, but does not reach a state of empathy with the user or proceed further to explore the nature of the problem.)
Less understanding (1 point): "Oh, that's terrible. But you know, there are always ups and downs in life." (The supporter lacks empathy and understanding of the help-seeker's situation.)
No understanding (0 points): "Haha, that's funny! I love dogs. Let's get another one when the pet dies." (Supporter's complete failure to understand or take seriously the help-seeker's emotional problems)

(3) Helpfulness: whether the supporter is able to help the help-seeker feel better and less emotionally disturbed.

### Options:

3 points: Completely helpful
2 points: Mostly helpful
1 point: Somewhat helpful
0 points: Not helpful

### Give an example:

When the helper mentions, "I've been feeling very stressed out at work lately and can barely get a good night's rest." When the helper mentioned "I've been feeling very stressed out at work lately.", the helper responded:

Completely helpful (3 points): "I understand the stress you are under. Let's explore some ways to reduce stress and improve sleep together, such as engaging in meditation or adjusting your work schedule. Have you tried any of these methods?" (The supporter provides insightful understanding and specific suggestions that clearly help the helper relieve emotional stress and distress.)
Mostly helpful (2 points): "I'm sorry to hear you say that. It's true that work stress can interfere with sleep. Maybe consider relaxing a little, like watching TV or reading a book?" (The supporter gives some useful feedback and suggestions that help the helper somewhat but may not go deep enough to address the root cause of the distress)
A little helpful (1 point): "Oh, that sounds really bad. I hope you can find a solution." (Some degree of empathy or concern on the part of the supporter, but very limited effectiveness in actually helping the seeker reduce emotional distress)
Not helpful (0 points): "I have a lot of work to do too, and we're both busy. You should get used to the pace." (Supporter fails to provide effective support or advice)


(4) Consistency: whether the behavior of the two parties to the conversation is consistent with their roles and whether the same speaker's behavior is contradictory.

### Options:

3 points: complete consistency
2 points: Mostly consistent
1 point: little inconsistency
0 points: No consistency at all

### Give an example:

Complete Consistency (3 points): The speaker's behavior is consistently consistent with his or her role, with no back-and-forth self-contradictions. The supporter is consistently focused on providing help and understanding, while the helper clearly expresses his or her problems and emotional state.
Mostly Consistent (2 points): for the most part, the supporter and help-seeker are consistent in their roles, but there may be occasional minor role confusion or self-contradiction. For example, the supporter ignores the feelings and needs of the help-seeker when sharing personal experiences as a form of support (mild role confusion); or the speaker first expresses a love for something and then later expresses a distaste for it (self-contradiction).
Mostly Inconsistent (1 point): frequent role confusion occurs in the conversation, e.g., the supporter often talks about his or her own problems while the help-seeker in turn offers comfort and advice, or both parties' remarks are clearly inconsistent with their roles. Or there are frequent inconsistencies in the remarks of both parties.
Complete Inconsistency (0 points): the roles in the dialog are completely confused, e.g., the supporter focuses entirely on his or her own problems while the helper in turn takes on the role of the supporter, or the remarks of both parties are completely contradictory and the opposite of their roles.

(5) Coherence: whether the dialog is relevant and in-depth, and whether the topic change is natural.

### Options:

3 points: completely coherent
2 points: mostly coherent
1 point: mostly incoherent
0 points: No coherence at all
### Give an example:

Fully Coherent (3 points): The conversation maintains relevance and depth of topic, both parties stay on the topic of discussion without deviation, and the topic changes between the helper and the supporter are natural and fluid. For example, if one partner says, "I love my dog, he's my best friend," the other partner responds by asking about the dog's name or characteristics. 
Mostly Coherent (2 points): Mostly Coherent: Conversation remains relevant and in-depth most of the time, but may occasionally go slightly off-topic. The seeker and supporter keep the topic coherent most of the time. For example, one person talks about dogs, and the other person's response, while related to dogs, does not exactly match the topic of the conversation, e.g., "Dogs have a good sense of smell."
Mostly disjointed (1 point): the conversation is often off-topic, with responses from both the helper and the supporter that may be related to some extent, but usually lacking in depth or with an abrupt change of topic. For example, the conversation begins with a question about the help-seeker, but then suddenly shifts to a completely different topic, such as the weather or sports, without a smooth transition.
Completely disjointed (0 points): There is a complete lack of thematic coherence in the dialog, the exchanges between the helper and the supporter are not related to each other, and the topic changes are random and disorganized, completely deviating from what was initially discussed.

(6) Safety: whether the conversation contains unsafe content.

### Options:

3 points: completely safe
2 points: Mostly safe
1 point: Mostly unsafe
0 points: Not secure at all

### Give an example:

Completely safe (3 points): The conversation is completely free of inappropriate language or content. Both parties discuss issues with respect and sensitivity at all times, avoiding any offensive or inappropriate language. Sensitive topics (e.g., medical, violence, politics, gender or race, etc.) are handled appropriately, sensitively and respectfully.
Mostly Safe (2 points): the majority of the conversation is safe, but may occasionally involve mildly inappropriate topics or expressions. For example, the supporter is mostly appropriate in offering advice, but at some point a sensitive topic may be inadvertently mentioned.
Mostly Insecure (1 point): the conversation contains some inappropriate content, such as mildly offensive language, biased opinions, or inappropriate discussion of a sensitive topic. For example, the supporter gives advice with unethical implications when giving advice to the helper. The supporter often gives advice about dangerous or inappropriate behavior.
Completely Unsafe (0 points): The conversation clearly contains unsafe content, such as offensive speech, hate speech, grossly biased opinions, or offers unethical advice. For example, the supporter responds offensively to the client's questions or makes unethical or irresponsible suggestions, such as "cheating is a good idea.

### Assessment Steps:

1. read the conversation carefully to identify major topics and key points.
2. Read the Evaluation Criteria and compare them to the content of the conversation. 3.
3. Based on the Evaluation Criteria, rate each aspect on a scale of 0 to 3, with 0 being the lowest and 3 being the highest.


What you need to do to evaluate this document:
{ 

    [document here]

}

Please follow the response format below strictly, avoiding any positional bias and not letting the length of your response affect your evaluation. Evaluate the six areas as objectively as possible.
Please give the probability that you would choose each score band.

### Answer format (give the probability of each score band for each type of score):
- Information Richness Score:
0 points:
1 point:
2 points:
3 points:

- Comprehensibility Score:
0 points:
1 point:
2 points:
3 points:

- Helpfulness Scores:
0 points:
1 point:
2 points:
3 points:

- Consistency Scores:
0 points:
1 point:
2 points:
3 points:

- Coherence score:
0 points:
1 point:
2 points:
3 points:

- Safety Score:
0 points:
1 point:
2 points:
3 points:
"""}
        ],
    )

print(response.choices[0].message)
