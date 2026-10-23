# R098EQP

## Descrição

Equipamentos

---

## Resumo

- Campos: 22
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| NomEqp | String(200) | Sim | Descrição do Equipamento |
| CodFab | Number(008,0) | Sim | Fabricante |
| PeqBru | Number(008,2) | Sim | Peso Bruto do Equipamento |
| PeqMin | Number(008,2) | Sim | Peso Mínimo do Equipamento |
| CapEqp | String(015) | Sim | Capacidade do Equipamento |
| DatFab | Date | Sim | Data da Fabricação |
| DatAqu | Date | Sim | Data da Aquisição |
| DatUso | Date | Sim | Data do Início do Uso |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| SitEqp | Number(001,0) | Sim | Situação do Equipamento |
| AtiFix | String(010) | Sim | Número do Ativo Fixo |
| NroSer | String(015) | Sim | Número de Série |
| ObsEqp | String(250) | Sim | Observação do Equipamento |
| CodLcz | Number(004,0) | Sim | Código da Localização |
| IndEpc | String(001) | Sim | Identifica se o equipamento é um EPC |
| UsaHab | String(001) | Sim | Identifica se o equipamento requer habilitação para uso |
| LocEqp | String(060) | Sim | Descritivo do Local Físico do local do equipamento |
| CodFil | Number(006,0) | Sim | Código da Filial |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098EQP_001

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

