# R088USU

## Descrição

Usuários da Frota

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAlt | Date | Não | Data da Alteração do Usuário do Veículo |
| TipClb | Number(001,0) | Sim | Tipo de Usuário da Frota |
| NumEmp | Number(004,0) | Sim | Empresa do Colabolador Usuário do Veículo |
| TipCol | Number(001,0) | Sim | Tipo do Colabolador Usuário do Veículo |
| NumCad | Number(009,0) | Sim | Cadastro do Colabolador Usuário do Veículo |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| AceLiv | String(001) | Sim | Tem Acesso Livre |
| DatVal | Date | Sim | Data de Validade para Uso |
| HorVal | Number(005,0) | Sim | Hora de Validade para o Uso |
| CtrUsu | Number(001,0) | Sim | Tipo do Contrato do Usuário |

---

## Chave Primária

- PlaVei
- DatAlt

---

## Índices

### R088USUIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

### R088USUIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- CadOcr

---

## Relacionamentos

### IR_R088USU_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

