# R086OTE

## Descrição

Ocorrências - Testemunhas

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| OcoAct | Number(006,0) | Não | Código da Ocorrência |
| SeqTes | Number(002,0) | Não | Sequência da Testemunha |
| NomTes | String(040) | Sim | Nome Testemunha |
| EndTes | String(040) | Sim | Endereço Testemunha |
| CidTes | Number(007,0) | Sim | Código da Cidade Testemunha |
| BaiTes | Number(004,0) | Sim | Código do Bairro Testemunha |
| TelTes | String(020) | Sim | Número do Telefone Testemunha |
| CepTes | Number(008,0) | Sim | CEP Testemunha |
| UsaCAT | String(001) | Sim | Define se considera a testemunha na emissão da CAT |
| DddTel | Number(003,0) | Sim | Código DDD do telefone da testemunha |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone da testemunha |
| NumTes | String(005) | Sim | Número logradouro |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- SeqTes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OTE_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

