# R129DEF

## Descrição

Definições - Treinamento

---

## Resumo

- Campos: 107
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DefRes | String(001) | Sim | Permite Exclusão de Reservas |
| OrcUni | String(001) | Sim | Orçamento com Local Único |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Código do Local |
| EmpRes | Number(004,0) | Sim | Empresa do Responsável |
| TipRes | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável para Certificado Curso |
| MsgCon | String(100) | Sim | Mensagem do Convite Curso |
| OrgDef | Number(004,0) | Sim | Código da Tabela de Organograma |
| LocDef | Number(009,0) | Sim | Código Local Default para Reserva |
| OriDef | Number(001,0) | Sim | Origem Default para Reserva |
| McuDef | Number(003,0) | Sim | Motivo do Curso Default para Reserva |
| VagDef | Number(006,0) | Sim | Vagas Default para Reserva |
| CheLoc | String(001) | Sim | Checar Local da Reserva |
| AceDem | String(001) | Sim | Aceitar participantes demitidos na formação de turma |
| CuaCip | Number(009,0) | Sim | Código do Curso da Cipa |
| CuaBri | Number(009,0) | Sim | Código do Curso da Brigada |
| TstAut | String(001) | Sim | Teste Automático na Definição Turma |
| NtrAut | String(001) | Sim | Item Nota Automático na Definição Turma |
| ReiAut | String(001) | Sim | Recurso Instrucional Automático na Definição Turma |
| RegRes | Number(003,0) | Sim | Código da Regra para o Colaborador |
| RegExe | Number(003,0) | Sim | Regra para Exclusão de Participante da Turma |
| RegSub | Number(003,0) | Sim | Regra para Substituição de Participante da Turma |
| RegTrf | Number(003,0) | Sim | Regra para Transferência de Participante da Turma |
| AceAdm | String(001) | Sim | Aceitar Participantes em Turmas Antes da Admissão |
| ExcLis | String(001) | Sim | Exclui lista de espera quando se torna participante |
| DesCur | String(001) | Sim | Mostrar botão p/ lançamento de despesa por curso na turma |
| DesLoc | String(001) | Sim | Mostrar botão p/ lançamento de despesa por local na turma |
| DesCcu | String(001) | Sim | Mostrar botão p/ lançamento de despesa por centro de custo na turma |
| DesPar | String(001) | Sim | Mostrar botão p/ lançamento de despesa por participante na turma |
| RecCar | String(001) | Sim | Recalcular carga horária do participante ao avaliar turma |
| ModPar | String(011) | Sim | Modelo do Gerador Relatórios  Seleção Participantes |
| ModBo1 | String(011) | Sim | Modelo Gerador Relatórios do 1º Botão |
| ModBo2 | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão |
| ModBo3 | String(011) | Sim | Modelo Gerador Relatórios do 3º Botão |
| ModBo4 | String(011) | Sim | Modelo Gerador Relatórios do 4º Botão |
| NomBo1 | String(020) | Sim | Nome do 1º Botão |
| NomBo2 | String(020) | Sim | Nome do 2º Botão |
| NomBo3 | String(020) | Sim | Nome do 3º Botão |
| NomBo4 | String(020) | Sim | Nome do 4º Botão |
| NomBpa | String(020) | Sim | Nome do botão p/ impressão do modelo de participante |
| MsgAva | String(001) | Sim | Apresenta mensagens ao alterar frequência/notas na avaliação |
| ConPro | String(001) | Sim | Permite concluir turma provisória |
| InsDem | String(001) | Sim | Aceitar instrutores desligados na formação de turma |
| NumLot | Number(009,0) | Sim | Último nr. de lote gerado, alimentado pelo geração coletiva de autorização |
| CodMcu | Number(003,0) | Sim | Motivo padrão para geração de reserva através do PDI |
| GerAfa | Number(001,0) | Sim | Gerar afastamento durante o período do treinamento |
| SitAfa | Number(003,0) | Sim | Situação de afastamento durante o período do treinamento |
| AbrTip | String(100) | Sim | Abrangência de tipo de colaborador na geração de afastamentos |
| RegBo1 | Number(003,0) | Sim | Código da regra do 1º botão |
| RegBo2 | Number(003,0) | Sim | Código da regra do 2º botão |
| RegBo3 | Number(003,0) | Sim | Código da regra do 3º botão |
| RegBo4 | Number(003,0) | Sim | Código da regra do 4º botão |
| InsAdm | String(001) | Sim | Aceitar Instrutores em Turmas Antes da Admissão |
| NomBA1 | String(020) | Sim | Nome do 1º Botão que será disponibilizado na tela de Avaliar |
| NomBA2 | String(020) | Sim | Nome do 2º Botão que será disponibilizado na tela de Avaliar |
| NomBA3 | String(020) | Sim | Nome do 3º Botão que será disponibilizado na tela de Avaliar |
| ModBA1 | String(011) | Sim | Modelo Gerador Relatórios do 1º Botão |
| ModBA2 | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão |
| ModBA3 | String(011) | Sim | Modelo Gerador Relatórios do 3º Botão |
| RegBA1 | Number(003,0) | Sim | Código da regra do 1º botão |
| RegBA2 | Number(003,0) | Sim | Código da regra do 2º botão |
| RegBA3 | Number(003,0) | Sim | Código da regra do 3º botão |
| AgrAss | String(001) | Sim | Agrupar as perguntas da avaliação de reação por assunto |
| DefPes | String(001) | Sim | Define se mostra a coluna Peso na tela de avaliação de reação web |
| IteZer | String(001) | Sim | Aceitar itens de despesa zerados |
| RegInc | Number(003,0) | Sim | Regra para Inclusão de Participante da Turma |
| AprTmp | String(001) | Sim | Apresenta tempo de serviço na tela de histórico geral de cursos |
| TolDes | Number(005,0) | Sim | Tolerância na Entrada/Saída (Deslocamento) |
| RegPes | Number(003,0) | Sim | Regra de Consistência do Peso das Notas |
| ExcHor | String(001) | Sim | Gerar exceção de horário se houver conflito de horário |
| ExcIns | String(001) | Sim | Gerar exceção p/ instrutor se houver conflito de horário |
| ExcSal | String(001) | Sim | Gerar exceção p/ sala se houver conflito de horário |
| ExcPar | String(001) | Sim | Gerar exceção p/ participante se houver conflito de horário |
| FreIns | String(001) | Sim | Controla Frequência dos Instrutores |
| McuInd | String(001) | Sim | Permite especificar motivo por participante no orçamento |
| OrcTre | Number(001,0) | Sim | Tipo de Orçamento |
| LibAvr | String(001) | Sim | Liberar a avaliação de reação automaticamente ao gerar |
| TexCon | String(2000) | Sim | Texto do Convite |
| ConAvr | String(001) | Sim | Concluir avaliação de reação ao avaliar a turma. |
| ApuFre | Number(001,0) | Sim | Apurar frequência ao consistir turma ou participante |
| LisNot | String(001) | Sim | Define como apresentará as notas na avaliação de reação |
| MosCod | String(001) | Sim | Define se apresentará o código das perguntas e respostas nas avaliações de reação/eficácia (WEB) |
| NomCoo | Number(001,0) | Sim | Especifica como deve ser apresentado o nome do coordenador da turma |
| RepRes | String(001) | Sim | Permite repetir reservas individuais para o mesmo curso quando já existe outra atendida |
| AvaVen | String(001) | Sim | Apresenta avaliação de eficácia vencida como pendente |
| AvrVen | String(001) | Sim | Apresenta avaliação de reação vencida como pendente |
| UsaTLT | Number(001,0) | Sim | Define se a empresa utiliza rotina de TLT |
| FamTLT | String(003) | Sim | Código da família padrão para TLT |
| EntTLT | Number(008,0) | Sim | Código da Entidade padrão para turmas de TLT |
| ExcCur | Number(001,0) | Sim | Define se deve permitir excluir cursos no TRWEB |
| ExcCon | Number(001,0) | Sim | Define se deve permitir excluir conhecimentos no TRWEB |
| DatTLT | Date | Sim | Data padrão para Requisitos por Local |
| NomTL1 | String(020) | Sim | Nome do 1º Botão que será disponibilizado na tela de Definir Turmas TLT |
| NomTL2 | String(020) | Sim | Nome do 2º Botão que será disponibilizado na tela de Definir Turmas TLT |
| NomTL3 | String(020) | Sim | Nome do 3º Botão que será disponibilizado na tela de Definir Turmas TLT |
| NomTL4 | String(020) | Sim | Nome do 4º Botão que será disponibilizado na tela de Definir Turmas TLT |
| ModTL1 | String(011) | Sim | Modelo Gerador Relatórios do 1º Botão |
| ModTL2 | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão |
| ModTL3 | String(011) | Sim | Modelo Gerador Relatórios do 3º Botão |
| ModTL4 | String(011) | Sim | Modelo Gerador Relatórios do 4º Botão |
| RegTL1 | Number(003,0) | Sim | Código da regra do 1º botão |
| RegTL2 | Number(003,0) | Sim | Código da regra do 2º botão |
| RegTL3 | Number(003,0) | Sim | Código da regra do 3º botão |
| RegTL4 | Number(003,0) | Sim | Código da regra do 4º botão |
| ConTur | Number(001,0) | Não | Define como serão tratados os conflitos de horários e salas |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R129DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

