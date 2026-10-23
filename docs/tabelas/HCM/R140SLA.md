# R140SLA

## Descrição

Salas de Treinamento

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| DesSla | String(030) | Sim | Descrição da Sala de Treinamento |
| TipSla | Number(003,0) | Sim | Tipo da Sala de Treinamento |
| TipLoc | String(001) | Sim | Localização da Sala |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| IdeSla | String(020) | Sim | Identificação da Sala |
| NomPre | String(030) | Sim | Nome do Prédio |
| IdeDis | String(001) | Sim | Ao alocar a sala deve ser verificada sua disponibilidade |

---

## Chave Primária

- CodSla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SLA_002

**Tabela:** R140TSL

| Origem | Destino |
|--------|---------|
| TipSla | TipSla |

