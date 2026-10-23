# R167APB

## Descrição

BS - Pacote de Benefícios - Assistência

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPac | Number(004,0) | Não | Código do Pacote de Benefícios |
| DatIni | Date | Não | Data de início do vale |
| CodSeg | Number(008,0) | Não | Código da seguradora |
| CodPla | Number(003,0) | Não | Código do Plano |
| BenCom | String(001) | Sim | Indicar se o benefício é obrigatório |
| ConCol | String(001) | Sim | Indicar se benefício estará disponível para colaborador |
| ConDep | String(001) | Sim | Indicar se benefício estará disponível para dependente |
| GraPar | String(100) | Sim | Abrangência de grau de parentesco para qual estará disponível o benefício |

---

## Chave Primária

- CodPac
- DatIni
- CodSeg
- CodPla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R167APB_000

**Tabela:** R167CPB

| Origem | Destino |
|--------|---------|
| CodPac | CodPac |

### IR_R167APB_003

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodSeg | CodOem |
| CodPla | CodPla |

