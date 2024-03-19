clear
echo "Type any String"
read string

length=$(echo "$string" | wc -c)
nvowels=0
nconsonants=0
ndigits=0

while (( length > 1 ))
do
    length=$((length - 1))
    h=$(echo "$string" | cut -c $length) 
   
    case $h in
    [AaEeIiOoUu]) ((nvowels++))
    ;;

    [BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz])
    ((nconsonants++))
    ;;

    [0-9]) ((ndigits++))
    ;;
    esac
done

echo "Number of Vowels      : $nvowels"
echo "Number of Consonants  : $nconsonants"
echo "Number of Digits      : $ndigits"
