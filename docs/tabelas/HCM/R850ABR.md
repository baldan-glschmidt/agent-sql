# R850ABR

## Descrição

Abrangências dos Processos Off Line

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPoF | Number(003,0) | Não | Código do Processo Off Line |
| CodLot | Number(004,0) | Sim | Código de Lote de Colaboradores |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrTcl | String(100) | Sim | Abrangência de Tipo de Colaborador |
| AbrCad | String(100) | Sim | Abrangência de Colaborador |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrEsc | String(100) | Sim | Abrangência de Escala |
| AbrRlg | String(100) | Sim | Abrangência de Coletor |
| CodGrr | Number(003,0) | Sim | Código do Grupo de Coletores |

---

## Chave Primária

- CodPoF

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R850ABR_000

**Tabela:** R850POF

| Origem | Destino |
|--------|---------|
| CodPoF | CodPoF |

