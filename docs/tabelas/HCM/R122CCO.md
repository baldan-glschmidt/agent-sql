# R122CCO

## Descrição

Candidatos Externos - Currículo Compilado

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqCCO | Number(009,0) | Não | Sequência do Currículo Compilado |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| UltAtu | Number(014,6) | Sim | Data/Hora da última atualização do campo de pesquisa e currículo resumido |
| DthCan | Number(014,6) | Sim | Data/Hora da última atualização do registro do Candidato |
| CurCpl | String(40000) | Sim | Texto usado para pesquisa por palavra chave |
| CurRes | String(60000) | Sim | Currículo resumido do Candidato em formato HTML |

---

## Chave Primária

- SeqCCO

---

## Índices

### R122CCOIndice2

**Tipo:** Não unico

Campos:
- NumCan

### R122CCOIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
