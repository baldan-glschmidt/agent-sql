# R300DPR

## Descrição

Definições de Processo Automático de Relatório

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo Automático |
| UsaCCh | String(001) | Sim | Utiliza Cadastro de Chefias |
| UsaHPo | String(001) | Sim | Utiliza hierarquia de postos |
| NivOrg | Number(002,0) | Sim | Considera chefes do nível especificado do organograma |
| ChfSub | String(001) | Sim | Inclui as chefias abaixo do nível especificado (para enviar e-mail) |
| UsaTur | String(001) | Sim | Deve utilizar informação do Turno como ítem da abrangência |
| ConSub | String(001) | Sim | Considera os sub-locais da chefia na abrangência do relatório |
| AbrUsu | String(001) | Sim | Considera a abrangência do usuário/colaborador associado a chefia |
| ConPad | String(001) | Sim | Considera a definição da tela de entrada padrão |
| CadChe | String(001) | Sim | Cadastro do Chefe |
| CadSCh | String(001) | Sim | Cadastro do Sub-Chefe |
| CadSub | String(001) | Sim | Cadastro do Substituto |
| AtuDat | String(001) | Sim | Atualiza Data da Tela de Entrada |
| CodThp | Number(003,0) | Sim | Código do Tipo de hierarquia do posto de trabalho |
| NivHie | Number(002,0) | Sim | Considera ocupantes do nível especificado da hierarquia de Postos |
| ConAba | String(001) | Sim | Considerar os ocupantes alocados abaixo do nível especificado |
| ConAbr | String(001) | Sim | Considera a abrangência do ocupante do Posto de Trabalho |
| PosSup | String(001) | Sim | Enviar para ocupante do Posto Superior |
| ConDel | String(001) | Sim | Considerar delegações da hierarquia no envio do email |
| EnvSup | String(001) | Sim | Enviar somente para superior imediato |

---

## Chave Primária

- TipPat
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R300DPR_001

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

