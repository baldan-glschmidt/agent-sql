# R088PRO

## Descrição

Proprietários de Veículos

---

## Resumo

- Campos: 23
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do veículo |
| TipPro | Number(001,0) | Não | Tipo de proprietário do veículo |
| SeqPro | Number(002,0) | Não | Sequência do registro de proprietário |
| DatIni | Date | Sim | Data inicial do registro de proprietário |
| HorIni | Number(005,0) | Sim | Hora do início do registro de proprietário do veículo |
| NumEmp | Number(004,0) | Sim | Empresa do colabolador proprietário do veículo |
| TipCol | Number(001,0) | Sim | Tipo do colabolador proprietário do veículo |
| NumCad | Number(009,0) | Sim | Cadastro do colabolador proprietário do veículo |
| CadOcr | Number(009,0) | Sim | Cadastro do colaborador proprietário de outra unidade |
| TipDoc | Number(001,0) | Sim | Tipo do documento do proprietário visitante |
| NumDoc | String(020) | Sim | Número do documento do proprietário visitante |
| NumMat | String(015) | Sim | Matrícula do aluno proprietário do veículo |
| VeiLoc | String(001) | Sim | Veículo locado |
| EmpVei | Number(004,0) | Sim | Empresa proprietária do veículo |
| CodOem | Number(008,0) | Sim | Código da outra empresa proprietária (Terceiro/Parceiro) |
| NumCon | String(015) | Sim | Número do contrato de serviço da proprietária |
| TipCnt | Number(001,0) | Sim | Tipo do contrato do proprietário |
| AceLiv | String(001) | Sim | Tem acesso livre |
| EmpRsp | Number(004,0) | Sim | Empresa do colabolador responsável pelo veículo |
| TipRsp | Number(001,0) | Sim | Tipo do colabolador responsável pelo veículo |
| CadRsp | Number(009,0) | Sim | Cadastro do colabolador responsável pelo veículo |
| DatFim | Date | Sim | Data final do cadastro da propriedade do veículo |
| HorFim | Number(005,0) | Sim | Hora final do cadastro da propriedade do veículo |

---

## Chave Primária

- PlaVei
- TipPro
- SeqPro

---

## Índices

### R088PROIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

### R088PROIndice3

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc

### R088PROIndice4

**Tipo:** Não unico

Campos:
- NumEmp
- CadOcr

---

## Relacionamentos

Nenhum relacionamento cadastrado.
