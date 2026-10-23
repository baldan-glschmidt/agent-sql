# R083LAU

## Descrição

PPRA - Laudo

---

## Resumo

- Campos: 27
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| DatLau | Date | Não | Data do Laudo |
| HorLau | Number(005,0) | Não | Hora do Laudo |
| QuaAge | Number(011,5) | Sim | Quantificação do perigo/fator de risco |
| DesAva | String(1000) | Sim | Laudo |
| DesRes | String(500) | Sim | Resultado do laudo para fins previdenciários |
| ObsLau | String(500) | Sim | Observação |
| GraRis | Number(001,0) | Sim | Grau de Risco |
| HorTer | Number(005,0) | Sim | Hora de término da medição |
| CodOem | Number(008,0) | Sim | Código da empresa que fez o laudo |
| EmpRes | Number(004,0) | Sim | Código da empresa do reponsável pelo laudo |
| TipRes | Number(001,0) | Sim | Tipo de colaborador responsável pelo laudo |
| CadRes | Number(009,0) | Sim | Cadastro do responsável pelo laudo |
| TecUti | String(100) | Sim | Descrição da técnica utilizada |
| NivAca | Number(011,5) | Sim | Intensidade/concentração p/Nível de Ação |
| LimTol | Number(011,5) | Sim | Intensidade/Concentração considerado Limite de Tolerância |
| QtdDos | Number(006,2) | Sim | Dose |
| ResTra | String(500) | Sim | Resultado do laudo para fins trabalhistas |
| QuaCol | Number(011,5) | Sim | Quantificação perigo/fator de risco considerando fator de redução |
| QuaAte | Number(011,5) | Sim | Quantificação final do perigo/fator de risco |
| NomArq | String(250) | Sim | Arquivo das medições |
| IdeAgN | String(015) | Sim | Identificador do agente nocivo (Obsoleto) |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- DatLau
- HorLau

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083LAU_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083LAU_005

**Tabela:** R083AGT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodGru | CodGru |
| CodAgt | CodAgt |

