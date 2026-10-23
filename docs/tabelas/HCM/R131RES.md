# R131RES

## Descrição

Histórico Testes - Respostas questões

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de Início do Teste |
| HorIni | Number(005,0) | Não | Hora de Início do Teste |
| GruPer | Number(005,0) | Não | Grupo de Perguntas respondida |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| CodRes | Number(002,0) | Não | Código da Resposta |
| ResAss | String(001) | Sim | Resposta assinalada pelo Colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- GruPer
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R131RES_004

**Tabela:** R131HTE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| HorIni | HorIni |

### IR_R131RES_007

**Tabela:** R202RES

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |
| CodPer | CodPer |
| CodRes | CodRes |

