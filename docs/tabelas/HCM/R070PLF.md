# R070PLF

## Descrição

Acessos por Plano de Localização Física

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| IdtPes | String(023) | Não | Identificador da Pessoa |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| DatAcc | Date | Sim | Data do Acesso |
| HorAcc | Number(005,0) | Sim | Hora do Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento |
| NumDoc | String(020) | Sim | Número do Documento |

---

## Chave Primária

- IdtPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PLF_001

**Tabela:** R058PLF

| Origem | Destino |
|--------|---------|
| VerPlf | VerPlf |
| CodPlf | CodPlf |

