# lin467
Kansai-ben word detector

Japan is a country that is filled with many dialects. One specifically worth noting is the Kansai dialect, also referred to by other names such as the Osaka dialect, Kinki dialect, et cetera. This dialect is noteworthy due to its amount of verb conjugations that differ greatly from standard Japanese, as well as lexical entries that are also different. This project attempts to detect these non-standard words or dialectal words automatically, and replace them with an appropriate standard form.

## Results

The project resulted in an expected output. The collected data was collected through native Kansai dialect speakers, and were asked for both their recording in Kansai dialect and standard Japanese.

The expected output was:

- また & 会え & たら & いい & ね〜
- again & meet.POT.COND & really & great & FP}
- `It would be really great to meet again, right?'

One difficulty faced in this project is that in this particular dialect, particle dropping in sentences is very common. This often throws off trained systems due to the fact that particles allow for easier word segmentation. The heavy amount of particle dropping makes it difficult for systems such as UDPipe to distinguish between Chinese character word boundaries at times.

- 明日映画観に行こうって思ってる

This should be parsed with '明日', '映画', and '観' as the correctly split word segments.

Furthermore, this program could be improved by having a more precise Kansai dialect dictionary and having more provided data. The data at hand was provided by native speakers, but data collection from short stories and Yahoo! Answers could further increase the variety in provided data.

With this project, I would like to be able to translate between standard Japanese and the Kansai dialect and vice-versa. For example, allowing for a user to check if a sentence is from a Kansai speaker and then seeing what that would mean in standard Japanese could be beneficial. There are many Kansai dialect words that may be confusing to native speakers, and having a translation program could be useful in determining the meaning of words with slight nuances like final particles.
