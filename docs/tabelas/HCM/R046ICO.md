# R046ICO

## Descrição

Informações demonstrativo pagamento - Contas Bancárias

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| SeqCon | Number(002,0) | Não | Sequência |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| NumCon | Number(012,0) | Sim | Conta Bancária |
| DigCon | String(003) | Sim | Dígito da Conta Bancária |
| PerCon | Number(005,2) | Sim | Percentual da Conta Bancária |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- SeqCon

---

## Índices

### R046ICOIndice2

**Tipo:** Não unico

Campos:
- CodBan
- CodAge

---

## Relacionamentos

Nenhum relacionamento cadastrado.
