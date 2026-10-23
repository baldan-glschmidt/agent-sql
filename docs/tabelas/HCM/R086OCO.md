# R086OCO

## Descrição

Ocorrências

---

## Resumo

- Campos: 35
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| OcoAct | Number(006,0) | Não | Código da Ocorrência (Incidente ou Acidente) |
| DatAct | Date | Sim | Data da Ocorrência |
| HorAct | Number(005,0) | Sim | Hora da Ocorrência |
| DesLoc | String(060) | Sim | Especificação do Local da Ocorrência |
| DesAct | String(1000) | Sim | Descrição da Ocorrência |
| EspAct | Number(003,0) | Sim | Código Espécie |
| TipAct | Number(003,0) | Sim | Código Tipo Acidente Trabalho |
| CauAct | Number(003,0) | Sim | Causa Acidente |
| AgeLes | Number(003,0) | Sim | Código do Agente Causador |
| GraAci | String(001) | Sim | Gravidade do Acidente (Potencial da Lesão) |
| ObsAct | String(1000) | Sim | Anotações Acidente Trabalho |
| RegPol | String(001) | Sim | Registro Policial (S/N) |
| EmpRsp | Number(004,0) | Sim | Código da empresa do responsável |
| TipRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro Responsável Informações |
| TipLoc | Number(001,0) | Sim | Tipo de Local da Ocorrência |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| CodCid | Number(007,0) | Sim | Cidade |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| NumAci | Number(008,0) | Sim | Número de identificação da ocorrência |
| NecAna | String(001) | Sim | Necessidade Análise do Incidente/Acidente |
| TipDan | Number(001,0) | Sim | Tipo de Dano (1 - Pessoal / 2 - Material / 3 - Pessoais e Materiais / 4 - Meio-Ambiente) |
| CodInv | Number(006,0) | Sim | Código da Investigação |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local da Ocorrência (Organograma) |
| TipAci | Number(001,0) | Sim | Código para emissão da CAT |
| USU_Metodo | String(500) | Sim | Método |
| USU_Material | String(300) | Sim | Material |
| USU_MeiAmbTra | String(300) | Sim | Meio Ambiente de Trabalho |
| USU_Maquina | String(300) | Sim | Máquina |
| USU_Medicao | String(300) | Sim | Medição |
| USU_MaoObra | String(300) | Sim | Mão de Obra |
| USU_CodMaq | Number(004,0) | Sim | Código da máquina, equipamento ou ferramenta |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
