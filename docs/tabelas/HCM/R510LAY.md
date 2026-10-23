# R510LAY

## Descrição

Currículo Web - Layout por Idioma

---

## Resumo

- Campos: 50
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| TitCur | String(100) | Sim | Título do cabeçalho do currículo |
| TitPag | String(100) | Sim | Título da página de login |
| CfgReg | Number(005,0) | Sim | Configuração regional - define os separadores de datas e números |
| RotEma | String(050) | Sim | Rótulo do campo e-mail |
| DicEma | String(200) | Sim | Dica de preenchimento do email |
| RotCPF | String(050) | Sim | Rótulo do campo CPF |
| DicCPF | String(200) | Sim | Dica de preenchimento do CPF |
| RotSen | String(050) | Sim | Rótulo do campo senha |
| DicSen | String(200) | Sim | Dica de preenchimento da senha |
| TamSen | Number(002,0) | Sim | Tamanho máximo da senha |
| InsLog | String(10000) | Sim | Instruções de login |
| RotLog | String(050) | Sim | Rótulo do botão login |
| RotEsq | String(050) | Sim | Rótulo esqueci minha senha |
| RotNov | String(050) | Sim | Rótulo do botão Novo currículo |
| TitNov | String(100) | Sim | Título da janela de Pré-cadastro |
| RotSal | String(050) | Sim | Rótulo do botão Salvar da janela de Pré-cadastro |
| RotCan | String(050) | Sim | Rótulo do botão Cancelar da janela de Pré-cadastro |
| MsgFin | String(10000) | Sim | Mensagem de finalização do currículo |
| CplFin | String(200) | Sim | Complemento da mensagem de finalização |
| RotLin | String(050) | Sim | Rótulo do link de redirecionamento para tela de login |
| RotVag | String(050) | Sim | Rótulo do botão Vagas disponíveis |
| MosVag | String(001) | Sim | Indica se o botão Vagas disponíveis deve estar visível |
| CodRSP | Number(003,0) | Sim | Código da política de recuperação de senha |
| CapLog | Number(001,0) | Sim | Apresentar o CAPTCHA ao efetuar o login no currículo web. |
| CapPre | Number(001,0) | Sim | Apresentar o CAPTCHA na tela de Pré Cadastro do currículo web. |
| CapRec | Number(001,0) | Sim | Apresentar o CAPTCHA na recuperação de senha do currículo web. |
| CapTit | String(050) | Sim | Título da tela do CAPTCHA. |
| CapOp1 | String(100) | Sim | Texto para orientação de preenchimento do CAPTCHA. |
| CapOp2 | String(100) | Sim | Texto secundário para orientação de preenchimento do CAPTCHA. |
| CapLnk | String(100) | Sim | Texto apresentado no link que tem o objetivo de atualizar a imagem do CAPTCHA. |
| CapBtn | String(040) | Sim | Rótulo do botão que tem o objetivo de enviar o CAPTCHA para validação. |
| TamMin | Number(002,0) | Sim | Tamanho mínimo da senha |
| SimSen | Number(001,0) | Sim | Símbolos na senha |
| NumSen | Number(001,0) | Sim | Números na senha |
| LetSen | Number(001,0) | Sim | Letras na senha |
| CheTer | String(050) | Sim | Rótulo do checkbox do termo |
| LinTer | String(050) | Sim | Rótulo do link do checkbox do termo |
| TitTer | String(050) | Sim | Título da tela do termo |
| BtnAce | String(050) | Sim | Rótulo do botão de "Aceito" |
| BtnNao | String(050) | Sim | Rótulo do botão de "Não aceito" |
| BtnFec | String(050) | Sim | Rótulo do botão de "Fechar" |
| BtnRev | String(050) | Sim | Rótulo do botão de "Revogar" |
| TitRec | String(050) | Sim | Título da tela de confirmação (em caso de recusa) |
| BtnCan | String(050) | Sim | Rótulo do botão de "Cancelar" |
| BtnCon | String(050) | Sim | Rótulo do botão de "Confirmar" |
| CmpAu1 | String(050) | Sim | Campo Auxiliar 1 |
| CmpAu2 | String(050) | Sim | Campo Auxiliar 2 |
| CmpAu3 | String(050) | Sim | Campo Auxiliar 3 |

---

## Chave Primária

- CodPer
- IdiLay

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510LAY_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

