# R009AAP

## Descrição

Assinatura Espelho de Ponto - Aprovação

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ProApr | String(040) | Não | Protocolo Aprovação |
| NumEmp | Number(004,0) | Sim | Empresa do colaborador |
| TipCol | Number(001,0) | Sim | Tipo do colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador |
| DatCmp | Date | Sim | Competência |
| DatApr | Date | Sim | Data Aprovação |
| ProSol | String(040) | Sim | Protocolo Solicitação |
| AssApr | String(001) | Sim | Assinatura Aprovada |
| AssCan | String(001) | Sim | Assinatura Cancelada |
| DadCri | String(3000) | Sim | Dados Aprovação |
| CodMot | Number(002,0) | Sim | Motivo Rejeição |
| ObsMot | String(1000) | Sim | Observação da Aprovação |

---

## Chave Primária

- ProApr

---

## Índices

### R009AAPindice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatCmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
