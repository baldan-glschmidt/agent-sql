# R094LOC

## Descrição

Localizador

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Localizado |
| TipSup | Number(001,0) | Sim | Tipo de Superior Imediato |
| CadSup | Number(009,0) | Sim | Cadastro do Superior Imediato |
| TipSub | Number(001,0) | Sim | Tipo de Substituto |
| CadSub | Number(009,0) | Sim | Cadastro do Substituto |
| FonBee | String(020) | Sim | Fone do Beep |
| NroBee | String(020) | Sim | Número do Beep |
| NumTel | String(020) | Sim | Número do telefone para primeiro contato (principal) |
| NumCel | String(020) | Sim | Número do Celular |
| ComLoc | String(100) | Sim | Comentário da Localização |
| DddBee | Number(003,0) | Sim | Código DDD do beep |
| DdiBee | Number(003,0) | Sim | Código DDI do beep |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddCel | Number(003,0) | Sim | Código DDD do celular |
| DdiCel | Number(003,0) | Sim | Código DDI do celular |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
