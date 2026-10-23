from pyscript import document  # type: ignore #type: ignore from Google
 
def candidate_checker(e):
    club_members = ["manila martinez", "aurhea santiago", "rebecca vinco", "kate velo", "yna sabulao", "gabrielle chua"]

    f_name = document.getElementById('first name').value
    l_name = document.getElementById('last name').value
    candidate = f"{f_name.strip()} {l_name.strip()}" #from Google because original code given didn't work.
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.' ,
               f'Congratulations {candidate}! You are part of the OBMC Glee Club.')
    
    document.getElementById('result').innerHTML = messages[member_checker]