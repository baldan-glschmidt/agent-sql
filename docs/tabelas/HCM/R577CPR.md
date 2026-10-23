# R577CPR

## Descrição

Tabela de proficiências - Conceitos

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTpr | Number(004,0) | Não | Código da Tabela de proficiências |
| CodCPr | String(010) | Não | Conceito da tabela de proficiência |
| DesCpr | String(060) | Sim | Descrição do conceito |
| DetCpr | String(2000) | Sim | Descrição detalhada do conceito |
| FaiIni | Number(008,4) | Sim | Permite informar a faixa inicial do conceito |
| FaiFin | Number(008,4) | Sim | Permite informar a faixa final do conceito |
| PonCpr | Number(008,4) | Sim | Permite informar a pontuação do conceito |
| CorCPr | String(010) | Sim | Permite informar a cor que será exibida para este conceito |
| PerIni | Number(008,4) | Sim | Permite informar a faixa inicial do conceito em percentual |
| PerFin | Number(008,4) | Sim | Permite informar a faixa final do conceito em percentual |
| ImgCpr | Image | Sim | Permite definir uma imagem que representará o conceito |

---

## Chave Primária

- CodTpr
- CodCPr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577CPR_000

**Tabela:** R577PRO

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |

