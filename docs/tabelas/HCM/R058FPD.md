# R058FPD

## Descrição

Funções por Dispositivo

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodFnc | Number(002,0) | Não | Código da Função |
| TipFNC | Number(001,0) | Sim | Tipo de função |
| MsgAti | String(032) | Sim | Mensagem de Ativação |
| MsgCnf | String(032) | Sim | Mensagem de Confirmação |
| FncMsk | String(032) | Sim | Máscara da Função |
| UtiAcc | String(001) | Sim | Realiza Acionamentos |
| IgnNiv | String(001) | Sim | Ignora Nível |
| BioMtr | String(001) | Sim | Utiliza Crachá Mestre |
| IgnFxh | String(001) | Sim | Ignora Faixa Horária |

---

## Chave Primária

- CodDsp
- CodFnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
