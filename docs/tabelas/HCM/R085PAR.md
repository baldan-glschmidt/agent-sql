# R085PAR

## Descrição

Parametrizações Orçamento - Gerais

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpBCa | Date | Sim | Competência Base de Cálculo |
| CmpBVa | Date | Sim | Competência Base para considerar Vagas |
| SalAdm | Number(001,0) | Sim | Salário dos Admitidos |
| SalDem | Number(001,0) | Sim | Salários dos Demitidos |
| SalBas | Number(001,0) | Sim | Salário Base |
| NivAdm | String(005) | Sim | Nível Salarial para Admissão |
| NivDem | String(005) | Sim | Nível Salarial para Demissão |
| NivSal | String(005) | Sim | Nível Salarial para Salário Base |
| PerBas | Number(005,2) | Sim | % Salário Base |
| PerAdm | Number(005,2) | Sim | % Salário Admissão |
| PerDem | Number(005,2) | Sim | % Salário Demissão |
| AnoBas | Number(004,0) | Sim | Ano base de cálculo do orçamento |
| SitOrc | String(001) | Sim | Orçamento fechado p/manutenção |
| CmpBta | Date | Sim | Competência base para uso da tabela salarial |
| NivOrc | Number(001,0) | Sim | Não localizando um parâmetro p/local, procura no nível padrão |
| CmpIni | Date | Sim | Competência inicial do cálculo do orçamento |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PAR_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

