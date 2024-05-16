# Probability_Theory_Project - Helen Guo

# An Optimal Stopping Problem

Imagine you are trying to select a candidate from a pool of applicants. You have a fixed number of candidates to interview, let's say 𝑛 and you interview them one by one. After each interview, you must decide immediately whether to hire the candidate or move to the next one. Once you've moved on to the next candidate, you cannot return to a previous one. 

The goal is to maximize the probability of selecting the best candidate, assuming you can't accurately rank the candidates and can only determine if the current candidate is better than the previous ones.

The optimal strategy for this problem involves a specific stopping rule: reject the first 𝑛/𝑒 candidates and then select the first candidate who is better than all the previously interviewed candidates, where 𝑒 is the base of the natural logarithm (approximately 2.71828). This strategy is known as the optimal stopping rule, and the problem is colloquially referred to as the Secretary Problem [1].

# Expected Optimal Stopping Problem and Open Questions

In a modified of this optimal stopping problem, the goal shifts from maximizing the probability of selecting the best candidate to maximizing the expected score of the chosen candidate. Each candidate has a certain score associated with them, and the objective is to select the candidate with the highest expected score. 

If each person is a random variable from a uniform distribution, then the optimal stopping rule under the problem setup is: reject the first √n candidates and then select the first candidate who is better than all the previously interviewed candidates [2]. The completed derivation can be found in citation [2] section 9.2 and Uniform_Expected_Secretary_Problem.pdf in the repostiroy.

When candidates are random variables from other distributions, optimal stopping rules under the problem setup is difficult to solve for analytically [3]. We address the problem of maximizing the expected score of the chosen candidate under various distributions of candidates via simulation. 

# Example with Data

We first apply code to an example dataset of wine ratings with points scored from 1-100 [4]. Suppose you have very distinctive taste in wine and are trying to choose a wine for an upcoming celebration. You have a fixed number 𝑛 of possible wine selections and after each taste, you must decide immediately whether to select the wine. Since you are choosing among a high-demand selection of limited-production wines, if you delay your decision, someone else will surely purchase the selection before you get a chance to purchase it. 

The app calculates the expected score of the wine selected under different fractions of candidates used for 'training' (how many wines to reject before then selecting the next best candidate), different number of candidates, and different number of trials that are averaged over.

# App for Answering the Expected Optimal Stopping Problem for Customized User Data

The purpose of this app is to help users decide how much data to "train" on when faced with an optimization problem where the selection decision must be made in the spot. The app includes three parts:
1) showcases the example describes above
2) tests results under known parametric families (e.g., beta, normal, gamma)
3) allows users to enter their own data and explore the resulting solutions

Please see the video [here](https://youtu.be/oSu4OCGVWV4) for a tutorial: https://youtu.be/oSu4OCGVWV4

## How to Launch:

1. **Install Streamlit:** If you haven't already, install Streamlit by running:

   pip install streamlit

3. **Download the Script:** Copy the provided code into a Python script file (e.g., `optimal_stopping.py`).

4. **Launch the App:** Run the Streamlit app by executing the following commands in your terminal:

   streamlit run optimal_stopping.py

# Citations
[1] Dan Teague, How To Find a Spouse: A Problem in Discrete Mathematics with an Assist from Calculus, (2017). Available at <a href="https://courses.ncssm.edu/math/Talks/PDFS/Spouse.pdf">https://courses.ncssm.edu/math/Talks/PDFS/Spouse.pdf</a>

[2] Goel, A., & Zadeh, R. (2014, April). Lecture 8. MS&E 317/CS 263: Algorithms for Modern Data Models, Spring 2014, Stanford University. Palo Alto, California. Available at <a href="https://stanford.edu/~rezab/amdm/notes/lecture8.pdf">https://stanford.edu/~rezab/amdm/notes/lecture8.pdf</a>

[3] Sarkar, Jyotirmoy, Score-based Secretary Problem, (2018). Available at at <a href="https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/ad0bc930-ec29-4915-80ac-16843de42988/content">https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/ad0bc930-ec29-4915-80ac-16843de42988/content</a> 

[4] “Wine ratings.” 2019. TidyTuesday GitHub Repository. Available at <a href="https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-05-28">https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-05-28</a>
