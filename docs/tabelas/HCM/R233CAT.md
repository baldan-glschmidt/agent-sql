# R233CAT

## Descrição

Categoria de Eventos

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CatEvn | Number(003,0) | Não | Categoria do Evento |
| DesCEv | String(060) | Sim | Descrição da Categoria do Evento |
| GerHis | String(001) | Sim | Gerar histórico de aperfeiçoamento para participantes de eventos desta categoria |
| SugInf | Number(001,0) | Sim | Define a origem das informações sugeridas durante a inclusão de um evento |
| AvaRea | String(001) | Sim | Permite Avaliação de Reação |
| PraARe | Number(003,0) | Sim | Prazo em dias, para ocorrer a avaliação de reação |
| AvaEfi | String(001) | Sim | Permite Avaliação de Eficácia |
| QueEfi | String(005) | Sim | Código do questionário da avaliação de eficácia |
| IniAva | Number(003,0) | Sim | Tempo de observação após treinamento para liberar a avaliação de eficácia |
| PraAva | Number(003,0) | Sim | Quantidade de dias para efetuar a avaliação de eficácia |
| AvaPar | String(001) | Sim | Permite Avaliação de Participantes |
| MedCua | Number(005,2) | Sim | Média mínima que o participante deve obter para ser aprovado |
| ConFre | Number(001,0) | Sim | Define a forma de controlar a frequência do participante |
| FreCua | Number(005,2) | Sim | Percentual de frequência que o participante deve obter para ser aprovado |
| CriRep | Number(001,0) | Sim | Define se a reprovação será por média ou frequencia quando ambas estiverem abaixo do mínimo |
| ExiIns | String(001) | Sim | Indica se o evento deve exigir instrutor para cada horário. |
| MetEfi | Number(003,0) | Sim | Percentual mínimo para o evento ser considerado eficaz |

---

## Chave Primária

- CatEvn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
