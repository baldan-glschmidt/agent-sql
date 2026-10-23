# R014APD

## Descrição

Aviso Prévio Diferenciado

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatAlt | Date | Não | Data da Alteração do Aviso Prévio |
| SeqApd | Number(003,0) | Não | Sequência |
| DiaAvi | Number(003,0) | Sim | Dias Aviso Indenizado Diferenciado |
| SinIda | String(001) | Sim | Sinal de Idade |
| NroIda | Number(003,0) | Sim | Número de Anos |
| SinSer | String(001) | Sim | Sinal Tempo Serviço |
| NroSer | Number(003,0) | Sim | Meses de Serviço |
| ConAbr | Number(001,0) | Sim | Condição da idade e tempo de serviço |

---

## Chave Primária

- CodSin
- DatAlt
- SeqApd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014APD_001

**Tabela:** R014AVP

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |
| DatAlt | DatAlt |

