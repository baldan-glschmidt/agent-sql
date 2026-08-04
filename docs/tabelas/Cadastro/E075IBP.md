# E075IBP

## Descrição

Cadastros - Tabela do IBPT

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SigUfs | String(002) | Não | Sigla do estado |
| ValIni | Date | Não | Vigência Inicial de Validade |
| ValFim | Date | Não | Vigência Final de Validade |
| CodIte | String(015) | Não | Código informado na tabela do IBPT |
| CodExc | Number(003,0) | Sim | Código da exceção da classificação fiscal |
| TipIte | Number(002,0) | Não | Origem Código |
| DesIte | String(255) | Não | Descrição do item da tabela |
| PerNfe | Number(005,2) | Sim | Percentual de Imposto Nacional Federal |
| PerIfe | Number(005,2) | Sim | Percentual de Imposto Importado Federal |
| PerEst | Number(005,2) | Sim | Percentual de Imposto Estadual |
| PerMun | Number(005,2) | Sim | Percentual de Imposto Municipal |
| VerTab | String(020) | Sim | Versão da Tabela |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E075IBPIndex2

**Tipo:** Unico

Campos:
- CodEmp
- SigUfs
- CodIte
- CodExc
- TipIte
- ValIni
- ValFim

---

## Relacionamentos

Nenhum relacionamento cadastrado.
