# R134PUB

## Descrição

Turmas - Público Alvo

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código Turma |
| CodGru | Number(003,0) | Sim | Código do Grupo de Empresas |
| NumEmp | Number(004,0) | Sim | Número da empresa do lote |
| CodLot | Number(004,0) | Sim | Código do Lote |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrTcl | String(100) | Sim | Abrangência de Tipo de Colaborador |
| AbrCad | String(100) | Sim | Abrangência de Colaborador |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrCCu | String(100) | Sim | Abrangência de Centro de Custo |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrSal | String(100) | Sim | Abrangência de Estrutura Salarial |
| AbrCla | String(100) | Sim | Abrangência de Classe Salarial |
| AbrNiv | String(100) | Sim | Abrangência de Nível Salarial |
| AbrSit | String(100) | Sim | Abrangência de Situação |

---

## Chave Primária

- CodCua
- TmaCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134PUB_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

